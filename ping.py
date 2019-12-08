import asyncio
import nym_proxy
import proto
import util

server_id = "F9xzbjnMQVN4ZidcqN2ip9kVnI9wbS39aVayZGiMihY="

VARINT_TWO_BYTES = 0xfd
VARINT_FOUR_BYTES = 0xfe
VARINT_EIGHT_BYTES = 0xff
MAX_UINT16 = 2**16 - 1
MAX_UINT32 = 2**32 - 1
MAX_UINT64 = 2**64 - 1
assert MAX_UINT16 == 0xffff
assert MAX_UINT32 == 0xffffffff
assert MAX_UINT64 == 0xffffffffffffffff

def varint_to_bytes(value):
    if value < VARINT_TWO_BYTES:
        return bytes([value])
    elif value <= MAX_UINT16:
        return (bytes([VARINT_TWO_BYTES]) +
                value.to_bytes(2, byteorder="big"))
    elif value <= MAX_UINT32:
        return (bytes([VARINT_FOUR_BYTES]) +
                value.to_bytes(4, byteorder="big"))
    elif value <= MAX_UINT64:
        return (bytes([VARINT_EIGHT_BYTES]) +
                value.to_bytes(8, byteorder="big"))

async def read_varint(reader):
    value = await reader.read(1)
    value = int.from_bytes(value, byteorder="big")
    #print("value", value)
    if value < VARINT_TWO_BYTES:
        return value
    elif value <= MAX_UINT16:
        data = await reader.read(2)
    elif value <= MAX_UINT32:
        data = await reader.read(4)
    elif value <= MAX_UINT64:
        data = await reader.read(8)
    return int.from_bytes(data, byteorder="big")

def send(writer, request):
    data = request.SerializeToString()
    size_data = util.varint_to_bytes(len(data))
    writer.write(size_data + data)

async def read_response(reader):
    data_size = await util.read_varint(reader)
    data = await reader.read(data_size)
    #print("Data size:", data_size)
    #print("Received:", data)

    response = proto.types.Response()
    response.ParseFromString(data)
    return response

async def run_ping():
    reader, writer = await asyncio.open_connection('127.0.0.1', 9001)

    request = proto.types.Request(
        clients=proto.types.RequestGetClients())
    send(writer, request)

    request = proto.types.Request(
        flush=proto.types.RequestFlush())
    send(writer, request)

    responses = [await read_response(reader) for i in range(2)]
    response = next(response for response in responses
                    if response.WhichOneof('value') == 'clients')
    clients = response.clients.clients
    server = [client for client in clients if client.Id == server_id][0]
    print(server)

    message_data = b'{"command": "fetch_history", "id": null, "client": "4JEtSrKsonmBuDvxJ9nITSu7iC4f8reutXRAVugPgS4=", "data": ["mtovQPnUuCeAUJkhqZn5vJ99vxJYNGXoEn"]}'
    request = proto.types.Request(
        send=proto.types.RequestSendMessage(
            message=message_data, recipient=server))
    send(writer, request)

    request = proto.types.Request(
        flush=proto.types.RequestFlush())
    send(writer, request)

    responses = [await read_response(reader) for i in range(2)]

    messages = []
    while not messages:
        request = proto.types.Request(
            fetch=proto.types.RequestFetchMessages())
        send(writer, request)

        request = proto.types.Request(
            flush=proto.types.RequestFlush())
        send(writer, request)

        responses = [await read_response(reader) for i in range(2)]
        response = next(response for response in responses
                        if response.WhichOneof('value') == 'fetch')

        messages = response.fetch.messages

        await asyncio.sleep(0.1)

    print("Messages:", messages)

if __name__ == "__main__":
    asyncio.run(run_ping())

