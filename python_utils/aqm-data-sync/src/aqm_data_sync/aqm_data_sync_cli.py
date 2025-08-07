import os
from pathlib import Path

import typer

from aqm_data_sync.core import (
    UseCaseKey,
    TimeVaryingContext,
    UseCase,
    TimeVaryingSyncRunner,
)

os.environ["NO_COLOR"] = "1"
app = typer.Typer(pretty_exceptions_enable=False)


@app.command(name="time-varying")
def time_varying(
    dst_dir: Path = typer.Option(
        ..., "--dst-dir", help="Destination directory for sync."
    ),
    first_cycle_date: str = typer.Option(
        None,
        "--first-cycle-date",
        help="First cycle date in yyyymmdd format. Required if --use-case is not provided.",
    ),
    fcst_hr: int = typer.Option(0, "--fcst-hr", help="Forecast hour."),
    last_cycle_date: str = typer.Option(
        None,
        "--last-cycle-date",
        help="Last cycle date in yyyymmdd format. If not provided, defaults to 24 hours after --first-cycle-date.",
    ),
    use_case: UseCaseKey = typer.Option(
        UseCaseKey.UNDEFINED, "--use-case", help="Use case."
    ),
    max_concurrent_requests: int = typer.Option(
        3, "--max-concurrent-requests", help="Max concurrent requests."
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Dry run."),
    snippet: bool = typer.Option(
        False,
        "--snippet",
        help="If provided, download data for a single forecast cycle loop (e.g. one day).",
    ),
) -> None:
    kwds = dict(
        first_cycle_date=first_cycle_date,
        dst_dir=dst_dir,
        fcst_hr=fcst_hr,
        last_cycle_date=last_cycle_date,
        max_concurrent_requests=max_concurrent_requests,
        dry_run=dry_run,
        snippet=snippet,
    )
    if use_case == UseCaseKey.UNDEFINED:
        ctx = TimeVaryingContext(**kwds)
    else:
        ctx = UseCase.from_key(use_case, **kwds)
    runner = TimeVaryingSyncRunner(ctx)
    runner.run()


@app.command(name="srw-fixed")
def srw_fixed(
    dst_dir: Path = typer.Option(
        ..., "--dst-dir", help="Destination directory for sync."
    ),
    max_concurrent_requests: int = typer.Option(
        3, "--max-concurrent-requests", help="Max concurrent requests."
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Dry run."),
) -> None: ...


if __name__ == "__main__":
    app()
