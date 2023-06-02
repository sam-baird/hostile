import json
from pathlib import Path

import defopt

from hostile import lib


def dehost(*, fastq1: Path, fastq2: Path | None = None, index: Path = lib.BT2_INDEX_PATH, out_dir: Path = lib.CWD, threads: int = 8) -> None:
    """
    Dehost fastqs using minimap2

    :arg fastq1: path to fastq.gz file
    :arg fastq2: path to optional second fastq.gz file (for paired reads)
    :arg out_dir: output directory for decontaminated fastq.gz files
    :arg threads: number of threads to launch (0 = auto)
    :arg debug: show debug messages
    """
    checksums = lib.dehost_fastqs(fastq1, fastq2, index=index, out_dir=out_dir)
    print(json.dumps(checksums, indent=4))


def main():
    defopt.run(dehost, no_negated_flags=True)
