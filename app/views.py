from flask import render_template, flash
from app import app
from .forms import TaskForm, CompleteForm

# default route for viewing all tasks
@app.route('/', methods=['GET', 'POST'])
def base():
    tasks = getTasks(2)
    form = CompleteForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tests if the task has been marked as finished and if it has a success message is
        # displayed and if not, an error message is displayed
        try:
            completeTask(form.number.data)
            flash('The task has been marked as finished.')
        except:
            flash("An error occurred and the task was not marked as finished.")

    # renders the 'all.html' page instead of 'base.html' to incorporate the features needed for
    # displaying tasks and marking tasks as finished
    return render_template('all.html',
                           title='To-Do List',
                           active1='active',
                           active2='',
                           active3='',
                           active4='',
                           header='All Tasks',
                           tasks=tasks,
                           form=form)

# route for viewing incomplete tasks
@app.route('/incomplete', methods=['GET', 'POST'])
def incomplete():
    tasks = getTasks(0)
    form = CompleteForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tests if the task has been marked as finished and if it has a success message is
        # displayed and if not, an error message is displayed
        try:
            completeTask(form.number.data)
            flash('The task has been marked as finished.')
        except:
            flash("An error occurred and the task was not marked as finished.")

    return render_template('all.html',
                           title='Incomplete',
                           active1='',
                           active2='active',
                           active3='',
                           active4='',
                           header='Incomplete Tasks',
                           tasks=tasks,
                           form=form)

# route for viewing finished tasks
@app.route('/finished', methods=['GET', 'POST'])
def finished():
    tasks = getTasks(1)
    form = CompleteForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tests if the task has been marked as finished and if it has a success message is
        # displayed and if not, an error message is displayed
        try:
            completeTask(form.number.data)
            flash('The task has been marked as finished.')
        except:
            flash("An error occurred and the task was not marked as finished.")

    return render_template('all.html',
                            title='Finished',
                            active1='',
                            active2='',
                            active3='active',
                            active4='',
                            header='Finished Tasks',
                            tasks=tasks,
                            form=form)

# route for creating a new task
@app.route('/task', methods=['GET', 'POST'])
def task():
    form = TaskForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tests if the new task has been created and if it has a success message is
        # displayed and if not, an error message is displayed
        try:
            submitTask(form.title.data, form.date.data, form.description.data)
            flash('The task has been created.')
        except:
            flash("An error occurred and the task was not created.")

    return render_template('task.html',
                           title='New Task',
                           active1='e',
                           active2='',
                           active3='',
                           active4='active',
                           form=form)

# this function retrieves the relevant tasks from the database depending on whether all the
# tasks, the incomplete tasks or the finished tasks are required
def getTasks(option):
    from app import db, models
    import datetime

    if option == 2:
        return models.Task.query.all()

    else:
        return models.Task.query.filter_by(complete = option).all()

# this function marks the given task as completed
def completeTask(number):
    from app import db, models
    import datetime

    task = models.Task.query.get(number)
    task.complete = 1
    db.session.commit()

# this function adds the data about the new task to the database
def submitTask(title, date, description):
    from app import db, models
    import datetime

    newTask = models.Task(title=title, date=date, description=description, complete=0)
    db.session.add(newTask)
    db.session.commit()
