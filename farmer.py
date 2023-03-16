from flask import*
from database import DB,CR
farmer=Blueprint("farmer",__name__)

@farmer.route("/")
def farmerhome():
    return render_template("farmerhome.html")

@farmer.route("/answerquestion",methods=["post","get"])
def answerquestion():
    CR.execute("SELECT * FROM data")
    qanda=CR.fetchall()
    if 'submit' in request.form:
        answer=request.form['ans']
        id=request.form['submit']
        sql="UPDATE data SET  answer=%s WHERE id=%s"
        val=(answer,id)
        CR.execute(sql,val)
        DB.commit()
        flash("Answer submited")
        return redirect(url_for("farmer.answerquestion"))
    return render_template("answerquestion.html",qanda=qanda)

@farmer.route("/delete",methods=["post","get"])
def delete():
     CR.execute("SELECT *FROM data")
     res=CR.fetchall()
     if "submit" in request.form:
        id=request.form['submit']
        CR.execute("DELETE FROM data WHERE id=%s",(id,))
        DB.commit()
        flash("Items Delete")
        return redirect(url_for('farmer.delete'))
     return render_template('delete.html',res=res)





