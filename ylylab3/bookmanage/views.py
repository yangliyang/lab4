from django.shortcuts import render
from bookmanage.models import Book , Author
# Create your views here.
del
def play(books):
	book_list = []
	for book in books:
		author = Author.objects.get(AuthorID=book.AuthorID)
		bk = {}
		bk['author_name'] = author.Name
		bk['Publisher'] = book.Publisher
		bk['Price'] = book.Price
		bk['ISBN'] = book.ISBN
		bk['Title'] = book.Title
		book_list.append(bk)
	return book_list
	
def Home(req):
	books =Book.objects.all()
	book_list=play(books)
	return render(req,'Home.html',{'page':book_list})
def serch(req):
	name=req.GET.get( 'name')
	l=[]
	for i in Author.objects.all():
		if(i.Name==name):
			j=i.AuthorID
			for k in Book.objects.all():
				if(k.AuthorID==j):
					l.append(k)
	return render(req,'serch.html',{'l':l,'name':name})
def info(req,isdn):
	l={}
	for i in (Book.objects.all()):
		if(i.ISBN==isdn):
			l['Title']=i.Title
			l['ISBN']=i.ISBN
			l['AuthorID']=i.AuthorID
			l['Publisher']=i.Publisher
			l['PublishDate']=i.PublishDate
			l['Price']=i.Price
			j=Author.objects.get(AuthorID=i.AuthorID)
			l['name']=j.Name
			l['age']=j.Age
			l['country']=j.Country

	return render(req,'info.html',{'i':l})
def delete(req,isbn):
	page=Book.objects.all()
	for i in page:
		if(i.ISBN==isbn):
			i.delete()
	page=Book.objects.all()
	book_list=play(page)
	return render(req,'sucess.html',{})
def addbook(req):
	return render(req,'addbook.html',{})
def bookedit(req):
	isbn=req.GET.get( 'isbn')
	title=req.GET.get( 'title')
	authorid=req.GET.get( 'authorid')
	publisher=req.GET.get( 'publisher')
	publishdate=req.GET.get('publishdate')
	price=req.GET.get('price')
	i=Book(ISBN=isbn,Title=title,AuthorID=authorid,Publisher=publisher,PublishDate=publishdate,Price=price)
	i.save()
	for i in Author.objects.all():
		if(i.AuthorID==authorid):
			page=Book.objects.all()
			book_list=play(page)
			return render(req,'sucess.html',{})
	return render(req,'addauthor.html',{'authorid':authorid})
def changebook(req,isbn):
	ISBN=isbn
	return render(req,'changebook.html',{'ISBN':ISBN})
def bc(req,isbn):
	Isbn=req.GET.get( 'isbn')
	title=req.GET.get( 'title')
	authorid=req.GET.get( 'authorid')
	publisher=req.GET.get( 'publisher')
	publishdate=req.GET.get('publishdate')
	price=req.GET.get('price')
	for i in Book.objects.all():
		if (i.ISBN==isbn):
			i.ISBN=Isbn
			i.Title=title
			i.AuthorID=authorid
			i.Publisher=publisher
			i.PublishDate=publishdate
			i.Price=price
			i.save()
	for i in Author.objects.all():
		if(i.AuthorID==authorid):
			page=Book.objects.all()
			book_list=play(page)
			return render(req,'sucess.html',{})
	return render(req,'addauthor.html',{'authorid':authorid})
def addauthor(req,authorid):
	name=req.GET.get('name')
	age=req.GET.get('age')
	country=req.GET.get('country')
	i=Author(AuthorID=authorid,Name=name,Age=age,Country=country)
	i.save()
	page=Book.objects.all()
	book_list=play(page)
	return render(req,'sucess.html',{})

	