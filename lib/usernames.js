/*
 * usernames.js
 * Main script for the username generator.
 * Corpus is located in corpus.js, which is already loaded.
 */

function generateName() {
  let types = ["an", "aan", "aa", "adn", "vp", "dan", "pdn", "aca", "va", "vpn", "npn", "nn", "vcv"];
  switch (_.sample(types)) {
    case "an":
      return makeName(adjective, noun);
    case "aan":
      return makeName(adjective, adjective, noun);
    case "aa":
      return makeName(adverb, adjective);
    case "adn":
      return makeName(adverb, determiner, noun);
    case "vp":
      return makeName(verb, preposition);
    case "dan":
      return makeName(determiner, adjective, noun);
    case "pdn":
      return makeName(preposition, determiner, noun);
    case "aca":
      return makeName(adjective, conjunction, adjective);
    case "va":
      return makeName(verb, adverb);
    case "vpn":
      return makeName(verb, preposition, noun);
    case "npn":
      return makeName(noun, preposition, noun);
    case "nn":
      return makeName(noun, noun);
    case "vcv":
      return makeName(verb, conjunction, verb);
  }
}

function makeName() {
  let cats = [...arguments];
  let picked = _.map(cats, _.sample);
  let cap = _.map(picked, _.upperFirst);
  let username = _.join(cap, "");
  console.log(username);
  return username;
}

$(document).ready(() => {
  let $btn = $("<button />", {
    id: "generateBtn",
    class: "col s12 m6 offset-m3 l4 offset-l4 btn waves-effect waves-light",
    text: "Generate",
    click: () => {
      $("#username").text(generateName());
    }
  });
  let $row = $("<div />", {
    class: "row"
  });
  $row.append($btn);
  $("#content").append($row);
});
