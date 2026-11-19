import pytest

from src.job_scheduler import JobScheduler


def test_add_job():
    scheduler = JobScheduler()

    job = scheduler.add_job("Data Backup", 3)

    assert job.job_id == 1
    assert job.name == "Data Backup"
    assert scheduler.pending_jobs() == 1


def test_process_priority_order():
    scheduler = JobScheduler()

    scheduler.add_job("Backup", 3)
    scheduler.add_job("Security Alert", 1)
    scheduler.add_job("Report", 2)

    first = scheduler.process_next()
    second = scheduler.process_next()
    third = scheduler.process_next()

    assert first.name == "Security Alert"
    assert second.name == "Report"
    assert third.name == "Backup"


def test_same_priority_order():
    scheduler = JobScheduler()

    scheduler.add_job("First", 1)
    scheduler.add_job("Second", 1)

    assert scheduler.process_next().name == "First"
    assert scheduler.process_next().name == "Second"


def test_execution_history():
    scheduler = JobScheduler()

    scheduler.add_job("Task A", 2)
    scheduler.add_job("Task B", 1)

    scheduler.process_next()

    history = scheduler.execution_history()

    assert len(history) == 1
    assert history[0].name == "Task B"


def test_empty_scheduler():
    scheduler = JobScheduler()

    assert scheduler.process_next() is None
    assert scheduler.is_empty()


def test_invalid_job_name():
    scheduler = JobScheduler()

    with pytest.raises(ValueError):
        scheduler.add_job("   ", 1)

    with pytest.raises(TypeError):
        scheduler.add_job("Invalid Priority", 1.5)
