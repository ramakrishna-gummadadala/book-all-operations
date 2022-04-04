def editbook(request,book_id):

    queryset = Book.objects.filter(book_id=book_id)
    if request.POST:
        form=BookForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=BookForm(instance=queryset)
        template = 'editbook.html'
        book = { 'form':form }
    return render_to_response(template, book , RequestContext(request)) 
