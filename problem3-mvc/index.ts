import express from 'express'
import cors from "cors"
import { MySqlDataSource } from './datasources/MySqlDataSource'
import mainRouter from "./routers/index"

MySqlDataSource.connect()
const app = express()
app.use(express.json())
const port = process.env.NODE_ENV == 'test' ? 4000 : 3001
const corsOptions : cors.CorsOptions = {
  // allow requests from all origins only for testing
  origin: '*'   
}

app.use(cors(corsOptions))
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))

app.use('/', mainRouter)


app.listen(port, () => {
  console.log(`Backend app listening on port ${port}`)
})

export default app