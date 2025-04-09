"""
Legacy Adapter for SkyOptima
This module integrates legacy airline systems by mapping legacy data formats to the standardized schema used by SkyOptima.
"""

import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LegacyAdapter")

def map_legacy_booking(legacy_record):
    """
    Map a legacy booking record to the SkyOptima schema.
    :param legacy_record: dict, legacy booking data
    :return: dict, standardized booking record or None if mapping fails
    """
    try:
        standardized_record = {
            "booking_id": legacy_record.get("bk_id"),
            "passenger_name": legacy_record.get("name"),
            "flight_number": legacy_record.get("flt_no"),
            "booking_date": legacy_record.get("bk_date"),
            "class": legacy_record.get("class"),
            "price": float(legacy_record.get("fare", 0)),
            "status": legacy_record.get("status", "confirmed"),
            # IATA NDC fields
            "ndc_ticket_number": legacy_record.get("ticket_no", None),
            "one_order_reference": legacy_record.get("order_ref", None)
        }
        return standardized_record
    except Exception as e:
        logger.error("Error mapping legacy booking: %s", e)
        return None

if __name__ == "__main__":
    # Example legacy record
    legacy_record_example = {
        "bk_id": "L12345",
        "name": "John Doe",
        "flt_no": "AI202",
        "bk_date": "2024-01-15",
        "class": "Economy",
        "fare": "350.00",
        "status": "confirmed"
    }
    mapped_record = map_legacy_booking(legacy_record_example)
    print(json.dumps(mapped_record, indent=2))
