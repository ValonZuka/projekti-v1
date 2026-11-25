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



def test_invalid_priority():
    scheduler = JobScheduler()

    with pytest.raises(TypeError):
        scheduler.add_job("Invalid Task", 1.5)

        

def test_cancel_job():
    scheduler = JobScheduler()

    job1 = scheduler.add_job("Backup", 3)
    scheduler.add_job("Security Alert", 1)

    assert scheduler.cancel_job(job1.job_id) is True

    processed = scheduler.process_next()

    assert processed.name == "Security Alert"
    assert scheduler.process_next() is None


def test_cancel_nonexistent_job():
    scheduler = JobScheduler()

    assert scheduler.cancel_job(999) is False


def test_cancel_already_processed_job():
    scheduler = JobScheduler()

    job = scheduler.add_job("Report", 2)

    scheduler.process_next()

    assert scheduler.cancel_job(job.job_id) is False

def test_cancel_same_job_twice():
    scheduler = JobScheduler()

    job = scheduler.add_job("Backup", 2)

    assert scheduler.cancel_job(job.job_id) is True
    assert scheduler.cancel_job(job.job_id) is False
    assert scheduler.pending_jobs() == 0
    assert scheduler.is_empty()


def test_cancel_multiple_jobs():
    scheduler = JobScheduler()

    job1 = scheduler.add_job("Backup", 3)
    job2 = scheduler.add_job("Report", 2)
    job3 = scheduler.add_job("Security", 1)

    assert scheduler.cancel_job(job1.job_id) is True
    assert scheduler.cancel_job(job2.job_id) is True

    assert scheduler.pending_jobs() == 1

    processed = scheduler.process_next()

    assert processed.name == "Security"
    assert scheduler.pending_jobs() == 0
    assert scheduler.is_empty()


def test_process_after_multiple_cancellations():
    scheduler = JobScheduler()

    job1 = scheduler.add_job("Task A", 1)
    job2 = scheduler.add_job("Task B", 2)
    job3 = scheduler.add_job("Task C", 3)

    scheduler.cancel_job(job1.job_id)
    scheduler.cancel_job(job2.job_id)

    processed = scheduler.process_next()

    assert processed.name == "Task C"
    assert scheduler.process_next() is None
    assert scheduler.pending_jobs() == 0


def test_cancel_invalid_job_id():
    scheduler = JobScheduler()
    scheduler.add_job("Backup", 1)

    assert scheduler.cancel_job(True) is False
    assert scheduler.cancel_job("1") is False
    assert scheduler.cancel_job(None) is False


def test_execution_history_returns_copy():
    scheduler = JobScheduler()

    scheduler.add_job("Backup", 1)
    scheduler.process_next()

    history = scheduler.execution_history()
    history.clear()

    assert len(scheduler.execution_history()) == 1
