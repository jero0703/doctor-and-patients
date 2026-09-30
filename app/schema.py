from pydantic import BaseModel, EmailStr, Field


class DoctorCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    specialization: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    is_active: bool = True


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


class PatientCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=0)
    phone: str = Field(..., min_length=10, max_length=15)


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    phone: str

    class Config:
        from_attributes = True