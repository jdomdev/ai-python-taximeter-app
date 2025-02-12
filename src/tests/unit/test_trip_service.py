import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from trip_service import start_trip

def test_start_trip_with_immediate_end(capsys):
    """
    Test the start_trip function when the user ends the trip immediately.
    """
    # Simulate user input: end the trip immediately
    with patch('builtins.input', side_effect=['y', 'y']):
        # Simulate time passing: 10 seconds stopped
        with patch('trip_service.datetime') as mock_datetime:
            start_time = datetime.now()
            mock_datetime.now.side_effect = [start_time, start_time + timedelta(seconds=10)]

            # Call the function
            start_trip()

    # Verify the output
    captured = capsys.readouterr()
    assert "Trip started. Press Ctrl+C to exit at any time." in captured.out
    assert "Taxi is now stopped..." in captured.out
    assert "Calculating trip cost..." in captured.out
    assert "Time stopped: 10.00 seconds" in captured.out
    assert "Time moving: 0.00 seconds" in captured.out

def test_start_trip_with_movement(capsys):
    """
    Test the start_trip function when the taxi moves for some time.
    """
    # Simulate user input: start moving, then stop and end the trip
    with patch('builtins.input', side_effect=['n', 'y', 'y']):
        # Simulate time passing: 5 seconds stopped, then 5 seconds moving
        with patch('trip_service.datetime') as mock_datetime:
            start_time = datetime.now()
            mock_datetime.now.side_effect = [
                start_time,
                start_time + timedelta(seconds=5),
                start_time + timedelta(seconds=10)
            ]

            # Call the function
            start_trip()

    # Verify the output
    captured = capsys.readouterr()
    assert "Trip started. Press Ctrl+C to exit at any time." in captured.out
    assert "Taxi is now moving..." in captured.out
    assert "Calculating trip cost..." in captured.out
    assert "Time stopped: 5.00 seconds" in captured.out
    assert "Time moving: 5.00 seconds" in captured.out

def test_start_trip_with_multiple_states(capsys):
    """
    Test the start_trip function with multiple state changes (moving and stopping).
    """
    # Simulate user input: start moving, stop, then end the trip
    with patch('builtins.input', side_effect=['n', 'y', 'y']):
        # Simulate time passing: 5 seconds moving, then 5 seconds stopped
        with patch('trip_service.datetime') as mock_datetime:
            start_time = datetime.now()
            mock_datetime.now.side_effect = [
                start_time,
                start_time + timedelta(seconds=5),
                start_time + timedelta(seconds=10)
            ]

            # Call the function
            start_trip()

    # Verify the output
    captured = capsys.readouterr()
    assert "Trip started. Press Ctrl+C to exit at any time." in captured.out
    assert "Taxi is now moving..." in captured.out
    assert "Taxi is now stopped..." in captured.out
    assert "Calculating trip cost..." in captured.out
    assert "Time stopped: 5.00 seconds" in captured.out
    assert "Time moving: 5.00 seconds" in captured.out

def test_start_trip_with_continued_trip(capsys):
    """
    Test the start_trip function when the user chooses to continue the trip.
    """
    # Simulate user input: start moving, then continue without ending
    with patch('builtins.input', side_effect=['n', 'n']):
        # Simulate time passing: 5 seconds moving
        with patch('trip_service.datetime') as mock_datetime:
            start_time = datetime.now()
            mock_datetime.now.side_effect = [
                start_time,
                start_time + timedelta(seconds=5)
            ]

            # Call the function
            start_trip()

    # Verify the output
    captured = capsys.readouterr()
    assert "Trip started. Press Ctrl+C to exit at any time." in captured.out
    assert "Taxi is now moving..." in captured.out
    assert "Continuing the trip..." in captured.out
    assert "Calculating trip cost..." not in captured.out

def test_start_trip_with_invalid_input(capsys):
    """
    Test the start_trip function with invalid user input.
    """
    # Simulate user input: invalid input, then end the trip
    with patch('builtins.input', side_effect=['invalid', 'y', 'y']):
        # Simulate time passing: 10 seconds stopped
        with patch('trip_service.datetime') as mock_datetime:
            start_time = datetime.now()
            mock_datetime.now.side_effect = [
                start_time,
                start_time + timedelta(seconds=10)
            ]

            # Call the function
            start_trip()

    # Verify the output
    captured = capsys.readouterr()
    assert "Trip started. Press Ctrl+C to exit at any time." in captured.out
    assert "Taxi is now stopped..." in captured.out
    assert "Calculating trip cost..." in captured.out
    assert "Time stopped: 10.00 seconds" in captured.out
    assert "Time moving: 0.00 seconds" in captured.out