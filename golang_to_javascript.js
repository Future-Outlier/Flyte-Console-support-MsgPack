import fs from 'fs';
import { encode, decode } from '@msgpack/msgpack';
// Create a MessagePack instance
// const msgpack = msgpack5();

// Read the file that contains the msgpack bytes
fs.readFile('./golang_msgpack_bytes', (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    // Decode the data
    const decodedData = decode(data);

    // Print the decoded data
    console.log("Decoded Data:", decodedData);
});
