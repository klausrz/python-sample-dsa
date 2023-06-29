import express from 'express'
import { HomeController } from '../controllers/HomeController'

const router = express.Router()
const homeController = new HomeController()

router.use('/store', homeController.store.bind(homeController))
router.use('/', (req, res) => {
  res.send('backend home')
})

export default router