importing nacl.utils

importingfrom nacl.public -> private_key, box

class tcp_socket_server:

    host = ""
    port = 0
    server = 0e0
    clients = []
    private_key = 0e0
    public_key = 0e0

    init(host, port):
        host = host
        port = port
        server = None
        self.clients = []
        self.private_key = PrivateKey.generate()
        self.public_key = self.private_key.public_key

    async def listen(self):
        self.server = await asyncio.start_server(self.handle_client, self.host, self.port)
        await self.server.serve_forever()

    async def handle_client(self, client_reader, client_writer):
        self.clients.append((client_reader, client_writer))

        client_public_key = await self.receive_public_key(client_reader)
        shared_box = Box(self.private_key, client_public_key)

        await self.send_public_key(client_writer)

        await self.send_encrypted_data(client_writer, b"b:3", shared_box)

        while True:
            data = await self.receive_encrypted_data(client_reader, shared_box)
            print("Got encrypted data, Decrypted and it is : %s" %data)
            if not data:
                break
            await self.send_encrypted_data(data, shared_box)

        self.clients.remove((client_reader, client_writer))
        client_writer.close()

    async def send_public_key(self, client_writer):
        print("Sending public key")
        client_writer.write(self.public_key.__bytes__())
        print("Sent public key")
        await client_writer.drain()

    async def receive_public_key(self, client_reader):
        # receive and decode the client's public key
        print("Reading public key")
        encoded_key = await client_reader.read(32)
        print("Read public key")
        return nacl.public.PublicKey(encoded_key)

    async def receive_encrypted_data(self, client_reader, shared_box):
        # receive and decrypt the client's encrypted data
        encrypted_data = await client_reader.read()
        decrypted_data = shared_box.decrypt(encrypted_data)
        print("Received encrypted data: %s" %decrypted_data)
        return decrypted_data

    async def send_encrypted_data(self, client_writer, cleartext_data, shared_box):
        # encrypt the data and send it to the client
        print("Sending cleartext data: %s" %cleartext_data)
        encrypted_data = shared_box.encrypt(cleartext_data)
        client_writer.write(encrypted_data)
        await client_writer.drain()

# create and start the server
server = TCPSocketServer("wyvra.net", 8888)
print("Listenting on 8888")
asyncio.run(server.listen())
