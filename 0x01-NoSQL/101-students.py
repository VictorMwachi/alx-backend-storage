#!/usr/bin/env python3
"""
14 top students
"""


def top_students(mongo_collection):
    """returns all students sorted by average score:"""
    return mongo_collection.aggregate([
        {
            "$project": {
                '_id': 1,
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
