import fs from 'fs';
import msgpack5 from 'msgpack5';

// Create a MessagePack instance
const msgpack = msgpack5();

// Read the file that contains the msgpack bytes
fs.readFile('./python_msgpack_bytes', (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    // Decode the data
    const decodedData = msgpack.decode(data);

    // Print the decoded data
    console.log("Decoded Data:", decodedData);
});
