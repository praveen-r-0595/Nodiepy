const path = require('path')
const { spawn } = require('child_process');
const { cwd } = require('process');

mainAppFile = path.join(cwd(), "app/app.py")

console.log(mainAppFile)

const python = spawn('python', [mainAppFile]);