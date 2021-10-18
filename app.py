"""Pet adoption application."""

import os
from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    """Displays all pets. Main homepage of Application"""
    pets = Pet.query.all()
    return render_template("pet-home.html", pets=pets)


@app.route("/new", methods=["GET", "POST"])
def pet_add():
    """Handles pet add form display, and add form validation and submission"""
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data,
                      photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash("Pet added successfully")
        return redirect("/")
    else:
        return render_template("pet-add-form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_edit(pet_id):
    """Handles pet edit form display, edit form validation and submission"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet.name} updated!")
        return redirect(f"/")
    else:
        return render_template("pet-edit-form.html", form=form)
