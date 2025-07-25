from __future__ import annotations

from pathlib import Path
from typing import Any

from polars._utils.various import is_path_or_str_sequence
from polars.io.partition import PartitionMaxSize


def _first_scan_path(
    source: Any,
) -> str | Path | None:
    if isinstance(source, (str, Path)):
        return source
    elif is_path_or_str_sequence(source) and source:
        return source[0]
    elif isinstance(source, PartitionMaxSize):
        return source._base_path

    return None


def _get_path_scheme(path: str | Path) -> str | None:
    path_str = str(path)
    i = path_str.find("://")

    return path_str[:i] if i >= 0 else None


def _is_aws_cloud(scheme: str) -> bool:
    return any(scheme == x for x in ["s3", "s3a"])


def _is_azure_cloud(scheme: str) -> bool:
    return any(scheme == x for x in ["az", "azure", "adl", "abfs", "abfss"])


def _is_gcp_cloud(scheme: str) -> bool:
    return any(scheme == x for x in ["gs", "gcp", "gcs"])
