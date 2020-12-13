
# Show the todos made by the user.
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user



from app import db,app
from app.database import Todo
from app.form import NewTodoForm, EditTodoForm

#展示所有待办
@app.route('/mytodos')
@login_required
def show_todos():
    incomplete = Todo.query.filter_by(writer=current_user, complete=False).all()
    complete = Todo.query.filter_by(writer=current_user, complete=True).all()
    return render_template('mytodos.html', incomplete=incomplete, complete=complete, title='My Todos')

#统计所有待办
@app.route('/statistics')
@login_required
def statistics():
    incomplete = Todo.query.filter_by(writer=current_user, complete=False).all()
    num1 = len(incomplete)
    complete = Todo.query.filter_by(writer=current_user, complete=True).all()
    num2 = len(complete)
    return render_template('statistics.html', num1=num1, num2=num2, title='My Todos')

#搜索
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    data = request.form.get('data')
    incomplete = db.session.query(Todo).filter(Todo.todo.like('%{0}%'.format(data)))
    incomplete = incomplete.filter_by(writer=current_user, complete=False).all()
    complete = db.session.query(Todo).filter(Todo.todo.like('%{0}%'.format(data)))
    complete = complete.filter_by(writer=current_user, complete=True).all()
    if data == None:
        data = ''
    return render_template('search.html', incomplete=incomplete, complete=complete, title='Search', data=data)


#新增待办
@app.route("/newtodo", methods=['GET', 'POST'])
@login_required
def create_todo():
    form = NewTodoForm()
    if form.validate_on_submit():
        todo = Todo(todo=form.todo.data, complete=False, writer=current_user)
        db.session.add(todo)
        db.session.commit()
        flash("Your todo has been created!", 'success')
        return redirect(url_for('show_todos'))
    return render_template('newtodo.html', title='New Todo', form=form)

#标记待办完成
@app.route('/complete/<todo_id>', methods=['GET', 'POST'])
@login_required
def complete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = True
    db.session.commit()
    flash('Todo Completed 🙌🏽!', 'success')
    return redirect(url_for('show_todos'))

#删除待办
@app.route('/delete/<todo_id>', methods=['GET', 'POST'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo Deleted', 'success')
    return redirect(url_for('show_todos'))

#编辑待办
@app.route('/edit/<todo_id>', methods=['GET', 'POST'])
@login_required
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    form = EditTodoForm()
    if form.validate_on_submit():
        todo.todo = form.todo.data
        db.session.commit()
        flash("Your todo has been update!", 'success')
        return redirect(url_for('show_todos'))
    form.todo.data = todo.todo
    return render_template('edittodo.html', title='Edit Todo',  form=form, id=todo_id)
