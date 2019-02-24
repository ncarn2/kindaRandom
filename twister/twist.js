const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Parse POST requests with JSON or URLEncoded
app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: true,
  }),
);

app.listen(process.env.PORT || 3000, () =>
  console.log(`Server listening on port ${process.env.PORT || 3000}`),
);

app.post('/bot', (req, res) => {
  const body = req.body;
  console.log(body);
});

