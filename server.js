const express = require("express");
const SerialPort = require("serialport");
const Readline = require("@serialport/parser-readline");

const app = express();
const PORT = 3000; // Adjust if needed
const ARDUINO_PORT = "COM5"; // Replace with your Arduino port

// Create a SerialPort object
const arduinoPort = new SerialPort(ARDUINO_PORT, { baudRate: 9600 });
const parser = arduinoPort.pipe(new Readline({ delimiter: "\n" }));

arduinoPort.on("open", () => {
    console.log("Serial Port Opened");
});

app.use(express.static("public"));

app.get("/trigger-buzzer", (req, res) => {
    // Send command to Arduino
    arduinoPort.write("START_FEEDBACK\n", (err) => {
        if (err) {
            console.error("Error on write: ", err.message);
            return res.status(500).send("Failed to send command to Arduino.");
        }
        console.log("Command sent to Arduino");
        res.send("Buzzer triggered!");
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
