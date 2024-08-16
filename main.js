const path = require('path')
const { spawn } = require('child_process');

mainAppFile = path.join(__dirname, "/app/app.py")

console.log(mainAppFile)


const pythonS = spawn('python', [mainAppFile]);

//pythonS.stderr.pipe(process.stderr);  //Run this if the window does'nt open