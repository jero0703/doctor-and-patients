from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Doctor, Patient
from app.schema import (
    DoctorCreate,
    DoctorResponse,
    PatientCreate,
    PatientResponse
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Doctor and Patient Management API",
    description="REST API for managing doctors and patients",
    version="1.0.0"
)


# =========================
# Doctor APIs
# =========================

@app.post(
    "/doctors",
    response_model=DoctorResponse,
    status_code=201
)
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):

    existing_doctor = db.query(Doctor).filter(
        Doctor.email == doctor.email
    ).first()

    if existing_doctor:
        raise HTTPException(
            status_code=400,
            detail="Doctor with this email already exists"
        )

    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email,
        is_active=doctor.is_active
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor


@app.get(
    "/doctors",
    response_model=list[DoctorResponse]
)
def get_doctors(db: Session = Depends(get_db)):

    return db.query(Doctor).all()


@app.get(
    "/doctors/{doctor_id}",
    response_model=DoctorResponse
)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):

    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor


# =========================
# Patient APIs
# =========================

@app.post(
    "/patients",
    response_model=PatientResponse,
    status_code=201
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        phone=patient.phone
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


@app.get(
    "/patients",
    response_model=list[PatientResponse]
)
def get_patients(db: Session = Depends(get_db)):

    return db.query(Patient).all()