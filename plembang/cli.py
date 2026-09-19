import argparse
import sys
from pathlib import Path

from . import __version__
from .runner import PalembangRunner
from .transpiler import PalembangTranspiler


def start_repl(runner: PalembangRunner, debug: bool = False) -> None:
    print("--------------------------------------------------------------")
    print(f"  Baso Plembang Engine v{__version__} (REPL Interactive)")
    print("  Ketik 'metu()' atau pencet Ctrl+C supayo metu.")
    print("--------------------------------------------------------------")

    runner.transpiler.keywords["metu"] = "quit"

    while True:
        try:
            user_input = input("plembang> ")
            if not user_input.strip():
                continue

            runner.run_code(user_input, debug=debug, filename="<REPL>")

        except (KeyboardInterrupt, EOFError):
            print("\nCacam nian! Program kau la sudem.")
            break


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="plembang",
        description="Transpiler & Runner Bahasa Pemrograman Baso Plembang",
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=str,
        help="Path ke file .plg (opsional, kosongkan untuk REPL)",
    )
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Tampilke kode Python hasil nge-transpile",
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    transpiler = PalembangTranspiler()
    runner = PalembangRunner(transpiler)

    if args.file:
        file_path = Path(args.file)
        if not file_path.is_file():
            print(f"Borok: File '{args.file}' dak nemu, lor!")
            sys.exit(1)

        # Proses pembacaan file diisolasi khusus untuk penanganan eror I/O
        try:
            source_code = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"Borok saat maco file: {e}")
            sys.exit(1)

        # Eksekusi dijalankan setelah file berhasil dibaca
        runner.run_code(source_code, debug=args.debug, filename=str(file_path))
    else:
        start_repl(runner, debug=args.debug)


if __name__ == "__main__":
    main()