showModal = (title, over, vote,poster,key) => {
    $("#label").text(title)
    url = 'https://image.tmdb.org/t/p/w500/' + poster
    $(".mod-img").attr("src", url)
    $("#img-desc").text(over)
    $("#img-category").text("Vote Average: " + vote)
    if(key != "None") {
        $(".trailer-link").attr("href",`/video/${key}`)
        $(".trailer-link").show()
    } else {
        $(".trailer-link").hide()
    }
    $("#myModal").modal("show")
}

// $(".trailer-link").attr("href", `https://www.youtube.com/watch?v=${key}`)
// 
