// creating a local server with the port number: 4000

const express = require('express')

const app = express()

const port_number = 4000

// middleware setup
app.use(express.json())

// database setup (MongoDB or dbeaver), 4/8/2024 or 4/15/2024

// route for Rawr related features
const userRoute = require('./routes/userRoute')
const vehicleRoute = require('./routes/vehicleRoute')
const employeeRoute = require('./routes/employeeRoute')
app.use('/employee',employeeRoute)
app.use('/user', userRoute)
app.use('/vehicle', vehicleRoute)


app.listen(port_number, () => {
    console.log(`server is running on http://localHost:${port_number}`)
})

// to run the backend server use `node index.js`