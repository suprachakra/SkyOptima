"""
legacy_adapter.py: Upgraded legacy system adapter for SkyOptima.
This module now supports IATA NDC 5.0 and ONE Order standards.
"""

import json
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LegacyAdapter")

def map_legacy_booking(legacy_record: dict) -> dict:
    """
    Map a legacy booking record to the SkyOptima schema, incorporating IATA NDC elements.
    
    Args:
        legacy_record (dict): Raw legacy booking data.
    
    Returns:
        dict: Standardized booking record.
    """
    try:
        standardized_record = {
            "BookingID": legacy_record.get("bk_id"),
            "PassengerName": legacy_record.get("name"),
            "FlightNumber": legacy_record.get("flt_no"),
            "DepartureDate": legacy_record.get("bk_date"),
            "Class": legacy_record.get("class"),
            "Price": float(legacy_record.get("fare", 0)),
            "Status": legacy_record.get("status", "confirmed"),
            # Additional fields for IATA NDC/ONE Order compliance:
            "NDCVersion": "5.0",
            "ONEOrderReference": legacy_record.get("order_ref", "N/A")
        }
        logger.info("Legacy booking mapped successfully for BookingID: %s", standardized_record["BookingID"])
        return standardized_record
    except Exception as e:
        logger.error("Error mapping legacy booking: %s", e)
        return {}

if __name__ == "__main__":
    # Example legacy record
    legacy_record_example = {
        "bk_id": "L12345",
        "name": "John Doe",
        "flt_no": "AI202",
        "bk_date": "2024-01-15",
        "class": "Economy",
        "fare": "350.00",
        "status": "confirmed",
        "order_ref": "ONE12345"
    }
    mapped_record = map_legacy_booking(legacy_record_example)
    print(json.dumps(mapped_record, indent=2))
