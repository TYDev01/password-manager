from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console
console = Console()
import sys
import getpass

def config():
    # Create a database
    db = dbconfig()
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE tydev")
    except Exception as e:
        printc("[red][!] An error occured while trying to create database")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database tydev created")

    # CREATE TABLES
    query = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'success' created ")

    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL )"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created ")

    master_pass = ""
    while 1:
        master_pass = getpass("Choose a Master Password")
