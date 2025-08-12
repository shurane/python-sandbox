from rich import print
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

# test samples

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

print("[bold red]Error:[/bold red] Something went wrong!")
print("Normal text and [green]green text[/green] in the same line.")

print("[bold underline magenta]Important:[/bold underline magenta] Backup your files!")
print("[yellow on black]High contrast text[/yellow on black]")

# interpolating

username = "Alice"
score = 95
print(f"[cyan]{username}[/cyan] scored [bold green]{score}[/bold green] points!")

# pretty print data structure

data = {"name": "Alice", "age": 30, "hobbies": ["reading", "cycling"]}
print(data)  # Automatically syntax-highlighted & pretty-printed

# table

console = Console()

table = Table(title="Scores")
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Score", style="green")

table.add_row("Alice", "95")
table.add_row("Bob", "88")

console.print(table)

# markdown

console = Console()
md = Markdown("# Hello World\nThis is **bold** and this is _italic_.")
console.print(md)