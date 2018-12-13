showModal = (title, over, vote,poster) => {
    alert("Hey")
    $("#label").text(title)
    url = 'https://image.tmdb.org/t/p/w500/' + poster
    $(".mod-img").attr("src", url)
    $("#img-desc").text(over)
    $("#img-category").text("Vote Average: " + vote)
    $("#myModal").modal("show")

}
copyUrl = () => {
    $("#url-to-copy").select()
    document.execCommand('copy');
    alert("Link copied")
}
