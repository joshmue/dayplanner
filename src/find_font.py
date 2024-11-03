import subprocess

def find_font(fontname):
    res = subprocess.run(
        ["fc-match", "-f", '%{file}', fontname],
        check=True,
        capture_output=True,
        encoding="UTF-8"
    )
    print(res.stdout)
    return str(res.stdout)