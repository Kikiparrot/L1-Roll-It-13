
def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# Main routine
make_statement("Hello world", "~")
make_statement("Round Results", "🎉")

