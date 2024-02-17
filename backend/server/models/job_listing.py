from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import date

from server.models.vet_classic import orelease, order

class JobListing(BaseModel):
    class Settings:
        name = "Job Listing"

    orelease: orelease
    order: order
    operations: any
    