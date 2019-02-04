var Tagger = require("./lib/brill_pos_tagger");

var base_folder = "/home/hugo/workspace/brill-pos-tagger";
var rules_file = base_folder + "/data/tr_from_pos.txt";
var lexicon_file = base_folder + "/data/lexicon.json";
var default_category = 'N';

var tagger = new Tagger(lexicon_file, rules_file, default_category, function(error) {
  if (error) {
    console.log(error);
  }
  else {
    var sentence = ["I", "see", "the", "man", "with", "the", "telescope"];
    console.log(JSON.stringify(tagger.tag(sentence)));
  }
});

