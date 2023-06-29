import mysql from 'mysql2/promise'


export class MySqlDataSource
{
  private static connection : any
  public static async connect()
  {
    if(!this.connection)
    {
      this.connection = await mysql.createConnection({
        host: '192.168.1.120',
        user: 'root',
        password: 'root',
        database: 'phoneshop'
      })
    }
    return this.connection
  }

}