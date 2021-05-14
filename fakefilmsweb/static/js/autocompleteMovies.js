$(function() {
    $("#id_movie_name").autocomplete({
        source: function(request, response) {
            $.ajax({
                url:'http://www.omdbapi.com/',
                dataType: "json",
                data: {
                    apikey: "4071f461",
                    t: request.term,
                    type: "movie"
                },
                success: function(data) {
                    data = {data};
                    response($.map(data, function(item) {
                        return {
                            label: item.Title,
                            year: item.Year,
                            category: item.Genre,
                        }
                    }))
                }
            })
        },
        minLength: 3,
        select: function(event, ui) {
            if(ui.item) {
                $("#id_movie_category").val(ui.item.category);
            }
        }
    })
})