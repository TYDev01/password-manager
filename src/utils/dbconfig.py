import mysql.connector

from rich import print as printc
from rich.console import Console
console = Console()

def config():
    try:
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'tydev',
            passwd = '2020'
        )
    except Exception as e:
        console.print_exception(show_locals=True)

    return db