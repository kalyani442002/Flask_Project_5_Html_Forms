from flask import Flask,render_template,request
FAI=Flask(__name__)

@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        '''form_data=request.form
        print(form_data)
        return form_data['na']'''
        fd=request.form
        return str(fd)
    return render_template('htmlforms.html')

if __name__=='__main__':
    FAI.run(debug=True)

