import os
import json
from datetime import datetime
import random

from flask import current_app
from app.config.features.photo_cycle import PHOTO_CYCLE_SETTINGS

import logging

LOG = logging.getLogger(__name__)


def get_refresh_details(subject):
    """
    Get the refresh details for the given subject.

    Args:
        subject (str): The subject for which to retrieve refresh details.

    Returns:
        dict: The refresh details for the given subject.

    Raises:
        KeyError: If refresh details are not found for the subject.
    """
    try:
        refresh_details = PHOTO_CYCLE_SETTINGS[subject]
    except KeyError:
        LOG.error(f"Refresh details not found for subject: {subject}")
        raise
    return refresh_details


def is_image_refresh_required(refresh_details):
    """
    Check if an image refresh is required based on the refresh details.

    Args:
        refresh_details (dict): The refresh details for the image.

    Returns:
        bool: True if image refresh is required, False otherwise.
    """
    current_date_in_secs = datetime.now().timestamp()
    last_refresh_date = refresh_details.get("last_refresh_date")
    cycle_interval = refresh_details.get("cycle_interval")
    return True if current_date_in_secs > last_refresh_date + cycle_interval else False


def generate_image_string(blueprint, subject):
    """
    Generate an image string based on the given blueprint and subject.

    Args:
        blueprint (str): The blueprint for the image.
        subject (str): The subject for the image.

    Returns:
        str: The generated image string.
    """
    last_id = PHOTO_CYCLE_SETTINGS[subject]["last_refresh_id"]
    seed = generate_random_image_index(blueprint, subject, last_id)
    return f"{subject}_{str(seed).zfill(3)}"


def update_refresh_details(blueprint, subject, id):
    """
    Update the refresh details for the given blueprint and subject.

    Args:
        blueprint (str): The blueprint for the image.
        subject (str): The subject for the image.
        id (int): The ID to update the refresh details with.
    """
    LOG.info(
        f"[PHOTO CYCLED][{blueprint}][internal_functions]:{subject} {PHOTO_CYCLE_SETTINGS[subject]['last_refresh_id']}"
    )
    PHOTO_CYCLE_SETTINGS[subject]["last_refresh_date"] = datetime.now().timestamp()
    PHOTO_CYCLE_SETTINGS[subject]["last_refresh_id"] = int(id)
    root_path = current_app.root_path
    config_file_path = os.path.join(root_path, "config", "features", "photo_cycle.py")

    with open(config_file_path, "w") as file:
        file.write(
            f"PHOTO_CYCLE_SETTINGS = {json.dumps(PHOTO_CYCLE_SETTINGS, indent=4)}"
        )


def get_img_string(blueprint, subject):
    """
    Get the image string for the given blueprint and subject.

    Args:
        blueprint (str): The blueprint for the image.
        subject (str): The subject for the image.

    Returns:
        str: The image string.

    Raises:
        KeyError: If refresh details are not found for the subject.
        Exception: If an error occurs while processing the image string.
    """
    LOG.info(f"BEFORE: {PHOTO_CYCLE_SETTINGS[subject]}")
    try:
        refresh_details = get_refresh_details(subject)
        if is_image_refresh_required(refresh_details):
            result = generate_image_string(blueprint, subject)
            update_refresh_details(blueprint, subject, result[-3:])
        else:
            original = f"{subject}_{str(refresh_details['last_refresh_id']).z

User
generate docstrings for these funcitons


def get_img_string(blueprint, subject):
    LOG.info(f"BEFORE: {PHOTO_CYCLE_SETTINGS[subject]}")
    try:
        refresh_details = get_refresh_details(subject)
        if is_image_refresh_required(refresh_details):
            result = generate_image_string(blueprint, subject)
            update_refresh_details(blueprint, subject, result[-3:])
        else:
            original = f"{subject}_{str(refresh_details['last_refresh_id']).zfill(3)}"
            return original
    except KeyError as e:
        LOG.error(
            f"KeyError occurred while processing image string for subject: {subject}. Error: {str(e)}"
        )
        return f"{subject}_000"
    except Exception as e:
        LOG.error(
            f"Error occurred while processing image string for subject: {subject}. Error: {str(e)}"
        )
        return f"{subject}_000"
    return result


def get_image_count(blueprint, subject):
    image_directory = os.path.join(current_app.static_folder, "img", blueprint, subject)
    image_files = os.listdir(image_directory)
    return len(image_files)


def generate_random_image_index(blueprint, subject, exclude_value):
    image_count = get_image_count(blueprint, subject)
    while True:
        seed = random.randint(0, image_count - 1)
        if seed != int(exclude_value):
            return seed
ChatGPT

Certainly! Here are the updated functions with the added docstrings:

python

def get_img_string(blueprint, subject):
    """
    Get the image string for the given blueprint and subject.

    Args:
        blueprint (str): The blueprint for the image.
        subject (str): The subject for the image.

    Returns:
        str: The image string.

    Raises:
        KeyError: If refresh details are not found for the subject.
        Exception: If an error occurs while processing the image string.
    """
    LOG.info(f"BEFORE: {PHOTO_CYCLE_SETTINGS[subject]}")
    try:
        refresh_details = get_refresh_details(subject)
        if is_image_refresh_required(refresh_details):
            result = generate_image_string(blueprint, subject)
            update_refresh_details(blueprint, subject, result[-3:])
        else:
            original = f"{subject}_{str(refresh_details['last_refresh_id']).zfill(3)}"
            return original
    except KeyError as e:
        LOG.error(
            f"KeyError occurred while processing image string for subject: {subject}. Error: {str(e)}"
        )
        return f"{subject}_000"
    except Exception as e:
        LOG.error(
            f"Error occurred while processing image string for subject: {subject}. Error: {str(e)}"
        )
        return f"{subject}_000"
    return result


def get_image_count(blueprint, subject):
    """
    Get the count of images for the given blueprint and subject.

    Args:
        blueprint (str): The blueprint for the images.
        subject (str): The subject for the images.

    Returns:
        int: The count of images.
    """
    image_directory = os.path.join(current_app.static_folder, "img", blueprint, subject)
    image_files = os.listdir(image_directory)
    return len(image_files)


def generate_random_image_index(blueprint, subject, exclude_value):
    """
    Generate a random image index for the given blueprint and subject.

    Args:
        blueprint (str): The blueprint for the image.
        subject (str): The subject for the image.
        exclude_value (int): The value to exclude from the random index generation.

    Returns:
        int: The generated random image index.
    """
    image_count = get_image_count(blueprint, subject)
    while True:
        seed = random.randint(0, image_count - 1)
        if seed != int(exclude_value):
            return seed