const http = require("http");
const data = require("C:/Administrator/it3038c-scripts/labs/widgets.json");

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data));
    }   else if (req.url === "/blue") {
        listBlue(res);
    }   else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end("Data not found");
    }
});

server.listen(3000);
console.log("Server is listening on port 3000")

const listBlue = (res) => {
    const colorBlue = data.filter((item) => {
        return item.color === "blue";
    });

    res.end(JSON.stringify(colorBlue));
}