import traceback
from typing import Any

from .transpiler import PalembangTranspiler


class PalembangRunner:
    """
    Engine untuk ngelola eksekusi kode, nangani eror yang ado di runtime,
    samo nampilke output debugging.
    """

    def __init__(self, transpiler: PalembangTranspiler) -> None:
        self.transpiler = transpiler

    def run_code(
        self, source_code: str, debug: bool = False, filename: str = "<stdin>"
    ) -> None:
        """
        Ngelakui transpile dan nge-eksekusi kode di dalem environment Python terisolasi.
        """
        try:
            python_code = self.transpiler.transpile(source_code)

            if debug:
                print("\n" + "=" * 15 + " HASIL PYTHON TRANSPILE " + "=" * 15)
                print(python_code)
                print("=" * 60 + "\n")

            global_scope: dict[str, Any] = {
                "__name__": "__main__",
                "__file__": filename,
            }

            code_obj = compile(python_code, filename, "exec")
            exec(code_obj, global_scope)  # noqa: S102

        except Exception as e:  # noqa: BLE001
            self._handle_error(e, filename)

    def _handle_error(self, exc: Exception, filename: str) -> None:
        """
        Format pesan eror supayo presisi nunjukke baris kode .plg yang bemasalah.
        """
        print(f"\n[Ado yang buak pas kode dijalanke`, lor: {exc.__class__.__name__}: {exc}]")

        if exc.__traceback__ is not None:
            tb = traceback.extract_tb(exc.__traceback__)
            for frame in tb:
                if frame.filename == filename:
                    print(f"  --> Ado di file '{filename}', baris {frame.lineno}: {frame.line}")