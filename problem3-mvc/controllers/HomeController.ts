// I'm using expressjs
import { Request, Response } from 'express'
import { MySqlDataSource } from '../datasources/MySqlDataSource';

export class HomeController
{
  public async store(req: Request, res: Response)
  {
    try {
      const connection = await MySqlDataSource.connect()
      const { manufacturer_id, model_id, imei, memory, manufacture_year, os_version, body_color,  price } = req.body;

      // I'm not using any libraries for validation as the validation rules are simple
      // Validate required fields
      if (!manufacturer_id || !model_id || !imei || !memory || !manufacture_year || !os_version) {
        return res.status(400).json({ error: 'manufacturer_id, model_id, imei, memory, manufacture_year, and os_version are required' });
      }

      // Validate data types
      if (
        typeof manufacturer_id !== 'number' || typeof model_id !== 'number' || typeof imei !== 'string' ||
        typeof memory !== 'number' || typeof manufacture_year !== 'number' || typeof os_version !== 'string'
      ) {
        return res.status(400).json({ error: 'Invalid data types' });
      }

      // Create a new phone object
      const phone = { manufacturer_id, model_id, imei, memory, manufacture_year, os_version, body_color, price };

      // Store the phone in the MySQL database
      await connection.query('INSERT INTO phones SET ?', phone)
      return res.status(201).json({ message: 'Phone stored successfully' })

    } catch (error: any) {
      console.error('Error storing phone');
      res.status(500).send(error.message)
    }
  }
}


// 1. How many customers do you currently have?
// I'm asking this to determine the size of the system and to 
// predict whether we'll need scaling in the future

// 2. Apart from registering the inventory, what do you hope 
// to achieve when using the web system? For example: generating reports, user visit statistics.
// I'm asking this to get a general sense of the shop manager's expectations, to find out 
// what his problems are so that I can provide him with suggestions on how
// the web system can automate his jobs and boost his productivity

// 3. There's a cool thing I'd like to suggest to you. Would you like 
// the web system to be your customer care staff? It could automatically answer 
// customer's questions related to your products. The system will take advantage
// of AI, ChatGTP in particular.

// I'm asking this because this feature can provide a lot of values to 
// the shop manager and reduce his human resource costs
