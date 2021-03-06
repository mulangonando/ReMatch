{
  "dataset": {
    "id": "qald-6-train-hybrid"
  },
  "questions": [
    {
      "id": "1",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Who was vice president under the president who approved the use of atomic weapons against Japan during World War II?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE { ?x text:\"approved the use of\" text:\"atomic weapons against Japan\" . ?x dbo:vicePresident ?uri . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Alben_W._Barkley"
              }
            } ] }
        }
      ]
    },
    {
      "id": "2",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "false",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "In which town was the man convicted of killing Martin Luther King born?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX dbp: <http://dbpedia.org/property/> PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {         res:Martin_Luther_King,_Jr. text:\"the man convicted of killing King\" ?x .         ?x dbo:birthPlace ?uri .         ?uri dbp:districtType \"Township\"@en . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Alton,_Illinois"
              }
            } ] }
        }
      ]
    },
    {
      "id": "3",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which anti-apartheid revolutionary was born in Mvezo?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         ?uri text:\"was a\" text:\"anti-apartheid revolutionary\" .         ?uri dbo:birthPlace res:Mvezo . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Nelson_Mandela"
              }
            } ] }
        }
      ]
    },
    {
      "id": "4",
      "answertype": "number",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "How many Golden Globe awards did the daughter of Henry Fonda win?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> SELECT ?n WHERE {         ?uri dbo:parent res:Henry_Fonda .         ?uri text:\"Golden Globe Awards\" ?n . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "n"
            ]
          },
          "results": { "bindings": [
            {
              "n": {
                "type": "literal",
                "value": "4"
              }
            } ] }
        }
      ]
    },
    {
      "id": "5",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which recipients of the Victoria Cross fought in the Battle of Arnhem?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {     ?uri dbo:award res:Victoria_Cross .    { ?uri text:\"fought in\" text:\"Battle of Arnhem\" . } UNION {?uri text:\"went into action\" text:\"Battle of Arnhem\"} } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/John_Hollington_Grayburn"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/John_Baskeyfield"
              }
            } ] }
        }
      ]
    },
    {
      "id": "6",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Where did the first human in space die?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX dbp: <http://dbpedia.org/property/> PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {         ?x dbp:type text:\"first human in space\" .         ?x dbo:deathPlace ?uri . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Kirzhach"
              }
            } ] }
        }
      ]
    },
    {
      "id": "7",
      "answertype": "number",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "How old was Steve Jobs' sister when she first met him?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> SELECT ?n WHERE {         res:Steve_Jobs dbo:relative ?uri . ?uri text:\"she did not meet until she was\" ?n . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "n"
            ]
          },
          "results": { "bindings": [
            {
              "n": {
                "type": "literal",
                "value": "25"
              }
            } ] }
        }
      ]
    },
    {
      "id": "8",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which members of the Wu-Tang Clan took their stage name from a movie?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         res:Wu-Tang_Clan dbo:bandMember ?uri .         ?uri text:\"stage name\" ?x .         ?x text:\"taken from\" text:\"film\" . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Ghostface_Killah"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Method_Man"
              }
            } ] }
        }
      ]
    },
    {
      "id": "9",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which writers had influenced the philosopher that refused a Nobel Prize?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         ?x rdf:type dbo:Philosopher .         ?x text:\"refuse\" text:\"Nobel Prize\" .         ?x dbo:influencedBy ?uri .         ?uri rdf:type dbo:Writer . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Gustave_Flaubert"
              }
            } ] }
        }
      ]
    },
    {
      "id": "10",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "false",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Under which king did the British prime minister that had a reputation as a playboy serve?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX yago: <http://dbpedia.org/class/yago/> SELECT DISTINCT ?uri WHERE {         ?x rdf:type yago:PrimeMinistersOfTheUnitedKingdom .         ?x text:\"reputation as a\" text:\"playboy\" .         ?x dbo:monarch ?uri . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/George_VI"
              }
            } ] }
        }
      ]
    },
    {
      "id": "11",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Who composed the music for the film that depicts the early life of Jane Austen?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         ?x rdf:type dbo:Film .         ?x text:\"depicts the early life of\" text:\"Jane Austen\" .         ?x dbo:musicComposer ?uri . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Adrian_Johnston"
              }
            } ] }
        }
      ]
    },
    {
      "id": "12",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "false",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Who succeeded the pope that reigned only 33 days?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX dbp: <http://dbpedia.org/property/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE { ?x rdf:type dbo:Pope . ?x text:\"reigned to\" text:\"his sudden death 33 days later\" . ?x dbp:predecessor ?uri . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Pope_John_Paul_II"
              }
            } ] }
        }
      ]
    },
    {
      "id": "13",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "false",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "On which island did the national poet of Greece die?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX yago: <http://dbpedia.org/class/yago/> SELECT DISTINCT ?uri WHERE {         ?x text:\"considered\" text:\"national poet of Greece\" .         ?x dbo:deathPlace ?uri .         ?uri rdf:type yago:Island109316454 . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Corfu"
              }
            } ] }
        }
      ]
    },
    {
      "id": "14",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which horses did The Long Fellow ride?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         ?x text:\"known as\" text:\"The Long Fellow\" .         ?x dbo:raceHorse ?uri . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/St._Paddy"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Petite_Etoile"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Alleged_(horse)"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Crepello"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Sir_Ivor"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Empery"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Nijinsky_(horse)"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/The_Minstrel"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Roberto_(horse)"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Never_Say_Die_(horse)"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Teenoso"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Royal_Academy_(horse)"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Rodrigo_de_Triano"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Shadeed"
              }
            } ] }
        }
      ]
    },
    {
      "id": "15",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Of the people that died of radiation in Los Alamos, whose death was an accident?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         ?uri dbo:deathPlace <http://dbpedia.org/resource/Los_Alamos,_New_Mexico> .         ?uri dbo:deathCause res:Acute_radiation_syndrome .         {?uri text:\"die from\" text:\"accident\" } UNION { ?uri text:\"was irradiated\" text:\"accident\" } } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Louis_Slotin"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Harry_K._Daghlian,_Jr."
              }
            } ] }
        }
      ]
    },
    {
      "id": "16",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which building owned by the Bank of America was featured in the TV series MegaStructures?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?uri WHERE {         ?uri rdf:type dbo:Building.         ?uri dbo:owner res:Bank_of_America .         ?uri text:\"featured on\" text:\"MegaStructures\" . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Bank_of_America_Tower_(New_York_City)"
              }
            } ] }
        }
      ]
    },
    {
      "id": "17",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which buildings in art deco style did Shreve, Lamb and Harmon design?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?uri WHERE {         ?uri dbo:architect <http://dbpedia.org/resource/Shreve,_Lamb_&_Harmon> .       { ?uri dbo:architecturalStyle res:Art_Deco . }       UNION       { ?uri text:\"style\" text:\"Art Deco\" . } UNION { ?uri text:\"ornamentation\" text:\"Art Deco\" . } }  "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Empire_State_Building"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Joel_W._Solomon_Federal_Building_and_United_States_Courthouse"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Hill_Building"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/500_Fifth_Avenue"
              }
            } ] }
        }
      ]
    },
    {
      "id": "18",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which birds are protected under the National Parks and Wildlife Act?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {     ?uri rdf:type dbo:Bird .     ?uri text:\"protected under\" text:\"National Parks and Wildlife Act\". } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Australian_Shelduck"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Chestnut_Teal"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Bar-shouldered_Dove"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Black-faced_Cuckoo-shrike"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Yellow_Thornbill"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Australian_Shoveler"
              }
            } ] }
        }
      ]
    },
    {
      "id": "19",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which country did the first known photographer of snowflakes come from?"
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?x WHERE {         ?uri text:\"is\" text:\"first known photographers of snowflakes\" .         ?uri dbo:birthPlace ?x .         ?x rdf:type dbo:Country . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/United_States"
              }
            } ] }
        }
      ]
    },
    {
      "id": "20",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "List all the battles commanded by the lover of Cleopatra."
        }
      ],
      "query": {
        "pseudo": " PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {     ?x text:\"love affair\" text:\"Cleopatra\".     ?uri dbo:commander ?x . } "
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Battle_of_Pharsalus"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Gallic_Wars"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Battle_of_Philippi"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Battle_of_Actium"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Antony's_Parthian_War"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Liberators'_civil_war"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Caesar's_Civil_War"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Battle_of_Mutina"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Final_War_of_the_Roman_Republic"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Sicilian_revolt"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Romanâ€“Persian_Wars"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Romanâ€“Parthian_Wars"
              }
            } ] }
        }
      ]
    },
    {
      "id": "21",
      "answertype": "boolean",
      "aggregation": "true",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Are the Rosetta Stone and the Gayer-Andersen cat exhibited in the same museum?"
        }
      ],
      "query": {
        "pseudo": "ASK WHERE { <http:/dbpedia.org/resource/Rosetta_Stone> text:\"public display at\" ?m1 . <http:/dbpedia.org/resource/Gayer-Anderson_cat> <http:/dbpedia.org/property/location> ?x . ?x rdfs:label ?m2 . FILTER (?m1=?m2) }"
      },
      "answers": [
        {
          "head": { } ,
          "boolean": true
        }
      ]
    },
    {
      "id": "22",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which actress starring in the TV series Friends owns the production company Coquette Productions?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { <http:/dbpedia.org/resource/Friends> <http:/dbpedia.org/ontology/starring> ?uri . ?uri text:\"owns\" text:\"a production company, called Coquette Productions\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Courteney_Cox"
              }
            } ] }
        }
      ]
    },
    {
      "id": "23",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Gaborone is the capital of which country member of the African Union?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri text:\"member of\" text:\"African Union\" . ?uri <http:/dbpedia.org/ontology/capital> <http:/dbpedia.org/resource/Gaborone> . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Botswana"
              }
            } ] }
        }
      ]
    },
    {
      "id": "24",
      "answertype": "date",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "When was the the greatest composer of Italian opera after Verdi born?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?date WHERE { <http:/dbpedia.org/resource/Madama_Butterfly> text:\"called\" text:\"the greatest composer of Italian opera after Verdi\" . ?x <http:/dbpedia.org/ontology/birthDate> ?date . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "date"
            ]
          },
          "results": { "bindings": [
            {
              "date": {
                "type": "literal",
                "value": "1858-12-22"
              }
            } ] }
        }
      ]
    },
{
      "id": "25",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "false",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which street basketball player was diagnosed with Sarcoidosis?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/StreetBasketballPlayers> . ?uri text:\"spent 22 days in a hospital\" text:\"Sarcoidosis\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Slick_Watts"
              }
            } ] }
        }
      ]
    },
    {
      "id": "26",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which daughter of Francis Ford Coppola received an Academy Award for Lost in Translation?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { <http://dbpedia.org/resource/Francis_Ford_Coppola> <http://dbpedia.org/ontology/child> ?x . ?x text:\"receive the Academy Award  for\" text:\"Lost in Translation\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Sofia_Coppola"
              }
            } ] }
        }
      ]
    },
    {
      "id": "27",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which city does the first person to climb all 14 eight-thousanders come from?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?x text:\"is\" text:\"first person to climb al fourteen eight-thousanders\" . ?x <http://dbpedia.org/ontology/birthPlace> ?uri . ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Settlement> . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Brixen"
              }
            } ] }
        }
      ]
    },
    {
      "id": "28",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Who is the wife of the creator of the CÃ©sar Award?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { <http://dbpedia.org/resource/CÃ©sar_Award> text:\"created by\" <http://dbpedia.org/resource/Georges_Cravenne> . <http://dbpedia.org/resource/Georges_Cravenne> <http://dbpedia.org/ontology/spouse> ?uri . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/FranÃ§oise_Arnoul"
              }
             }
	    ]
          }
        }
      ]
    },
    {
      "id": "29",
      "answertype": "boolean",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Did Napoleon's first wife die in France?"
        }
      ],
      "query": {
        "pseudo": "ASK WHERE { ?x text:\"first wife\" text:\"Napoleon\" . ?x <http://dbpedia.org/ontology/deathPlace> <http://dbpedia.org/resource/France> . }"
      },
      "answers": [
        {
          "head": { } ,
          "boolean": true
        }
      ]
    },
    {
      "id": "30",
      "answertype": "number",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "How old is James Bond in the latest Bond book by William Boyd?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?age WHERE { <http://dbpedia.org/resource/James_Bond> <http://dbpedia.org/ontology/lastAppearance> ?x . ?x <http://dbpedia.org/ontology/author> <http://dbpedia.org/resource/William_Boyd_(writer)> . ?x text:\"has\" ?age . FILTER (regex(?age, '.*years.*')) . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "age"
            ]
          },
          "results": { "bindings": [
            {
              "age": {
                "type": "literal",
                "value": "45"
              }
            } ] }
        }
      ]
    },
    {
      "id": "31",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "false",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "What eating disorder is characterized by an appetite for substances such as clay and sand?"
        }
      ],
      "query": {
        "pseudo": "SELECT ?uri WHERE { ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/EatingDisorders> . ?uri text:\"characterized by\" \"appetite for clay and sand\" .}"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Pica_(disorder)"
              }
            } ] }
        }
      ]
    },
    {
      "id": "32",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "What is the native city of Hollywood's highest-paid actress?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?x text:\"cited as\" text:\"Hollywod's highest-paid actress\" . ?x <http://dbpedia.org/ontology/birthPlace> ?uri . ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http:/dbpedia.org/ontology/City> .}"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Los_Angeles"
              }
            } ] }
        }
      ]
    },
    {
      "id": "33",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "In which city does the sports commentator known as Memory Man live?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?x text:\"is\" text:\"sports commentator\" . ?x text:\"known as\" text:\"Memory Man\" . ?x <http:/dbpedia.org/ontology/residence> ?uri ."
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Dublin"
              }
            } ] }
        }
      ]
    },
    {
       "id": "34",
       "answertype": "resource",
       "aggregation": "false",
       "onlydbo": "false",
       "hybrid": "true",
       "question": [
         {
           "language": "en",
           "string": "How many children does the actor who plays Dan White in Milk have?"
         }
       ],
       "query": {
         "pseudo": "SELECT ?n WHERE { <http://dbpedia.org/resource/Milk_(film)> <http://dbpedia.org/ontology/starring> ?uri . ?uri text:\"play\" text:\"Dan White\" . ?uri <http://dbpedia.org/property/children> ?n . }"
       },
       "answers": [
         {
           "head": {
             "vars": [
               "n"
             ]
           },
           "results": { "bindings": [
             {
               "n": {
                 "type": "literal",
                 "value": "2"
               }
            } ] }
        }
      ]
    },
    {
      "id": "35",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Who is the front man of the band that wrote Coffee & TV?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { <htp://dbpedia.org/page/Coffee_&_TV> <http://dbpedia.org/ontology/musicalArtist> ?x . ?x <http://dbpedia.org/ontology/bandMember> ?uri . ?uri text:\"is\" text:\"frontman\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Damon_Albarn"
              }
            } ] }
        }
      ]
    },
    {
      "id": "36",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which Chinese-speaking country is a former Portguese colony?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://dbpedia.org/ontology/language> <http://dbpedia.org/resource/Chinese_language>. ?uri a text:\"former Portuguese colony\".}"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Macau"
              }
            } ] }
        }
      ]
    },
    {
      "id": "37",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "What is the largest city in the county in which Faulkner spent most of his life?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { <http://dbpedia.org/resource/William_Faulkner> text:\"spent most of his life in\" ?x . ?x <http://dbpedia.org/ontology/largestCity> ?uri . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Oxford,_Mississippi"
              }
            } ] }
        }
      ]
    },
    {
      "id": "38",
      "answertype": "number",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "In which year did the Hungarian-American actor called \"The King of Horror\" make his first film?"
        }
      ],
      "query": {
        "pseudo": "SELECT ?year WHERE { ?x <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> text:\"Hungarian-American actor\" . ?x <http:/dbpedia.org/ontology/alias> \"The King Of Horror\" . ?x text:\"made his first film in\" ?year . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "year"
            ]
          },
          "results": { "bindings": [
            {
              "year": {
                "type": "literal",
                "value": "1917"
              }
            } ] }
        }
      ]
    },
    {
       "id": "39",
       "answertype": "string",
       "aggregation": "false",
       "onlydbo": "true",
       "hybrid": "true",
       "question": [
         {
           "language": "en",
           "string": "Under which pseudonym did Charles Dickens write some of his books?"
         }
       ],
       "query": {
         "pseudo": "SELECT DISTINCT ?string WHERE { ?x <http://dbpedia.org/ontology/author> <http://dbpedia.org/resource/Charles_Dickens> . ?x text:\"writing under the pseudonym of\" ?string . }"
       },
       "answers": [
         {
           "head": {
             "vars": [
               "string"
             ]
           },
           "results": { "bindings": [
             {
               "string": {
                 "type": "literal",
                 "value": "Boz"
               }
            } ] }
        }
      ]
    },
    {
      "id": "40",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "The home of the Mona Lisa is a landmark of which city?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { <http://dbpedia.org/resource/Mona_Lisa> <http://dbpedia.org/ontology/museum> ?x . ?x text:\"landmark of\" ?uri . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Paris"
              }
            } ] }
        }
      ]
    },
    {
      "id": "41",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "In which British territories was the \"Father of Singapore\" born?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { text:\"Father of modern Singapore\" <http://dbpedia.org/ontology/birthPlace> ?uri . ?uri rdf:type text:\"British territories\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Straits_Settlements"
              }
            } ] }
        }
      ]
    },
    {
      "id": "42",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which Secretary of State policies lead to the United States' acquisition of Pacific colonies?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://dbpedia.org/ontology/office> \"United States Secretary of State\" . ?uri text:\"policies lead\" text:\"United States' acquisition of Pacific colonies\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/James_G._Blaine"
              }
            } ] }
        }
      ]
    },
    {
      "id": "43",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Who are the architects of the tallest building in Japan?"
        }
      ],
      "query": {
	"pseudo": "SELECT DISTINCT ?uri WHERE { text:\"tallest building in Japan\" <http:/dbpedia.org/ontology/architect> ?uri . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Nikken_Sekkei"
              }
            } ,
             {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/CÃ©sar_Pelli"
              }
            }
            ] }
        }
      ]
    },
    {
      "id": "45",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "In which city where Charlie Chaplin's half brothers born?"
        }
      ],
      "query": {
        "pseudo": "SELECT ?uri WHERE { ?x text:\"half brother of\" <http:/dbpedia.org/resource/Charlie_Chaplin> . ?x <http:/dbpedia.org/ontology/birthPlace> ?y . ?y a <http:/dbpedia.org/ontology/Settlement> . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/London"
              }
            } ] }
        }
      ]
    },
    {
      "id": "46",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which German mathematicians were members of the von Braun rocket group?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://dbpedia.org/ontology/field> <http://dbpedia.org/resource/Mathematics> . ?uri <http://dbpedia.org/ontology/birthPlace> <http://dbpedia.org/resource/Germany> . ?uri text:\"member of\" text:\"von Braun rocket group\" . }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Walter_Haeussermann"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Oswald_Lange"
              }
            } ] }
        }
      ]
    },
    {
      "id": "47",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which writers converted to Islam?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Writer> . {?uri text:\"converted to\" text:\"Islam\" } Union {?uri text:\"became\" text:\"muslim\" }.}"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Jamilah_Kolocotronis"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Jacky_Trevane"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Ismael_Urbain"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Lev_Nussimbaum"
              }
            },
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Aukai_Collins"
              }
            } ] }
        }
      ]
    },
    {
      "id": "48",
      "answertype": "boolean",
      "aggregation": "true",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Are there man-made lakes in Australia that are deeper than 100 meters?"
        }
      ],
      "query": {
        "pseudo": "ASK WHERE {?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Lake> . ?uri <http://dbpedia.org/ontology/country> <http://dbpedia.org/resource/Australia> . ?uri text:\"is\" text:\"man-made\" . ?uri <http://dbpedia.org/ontology/depth> ?num . FILTER(?num > 10.0)}"
      },
      "answers": [
        {
          "head": { } ,
          "boolean": true
        }
      ]
    },
    {
      "id": "49",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which movie by the Coen brothers stars John Turturro in the role of a New York City playwright?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Film> . ?uri <http://dbpedia.org/ontology/director> <http://dbpedia.org/resource/Coen_brothers> . ?uri <http://dbpedia.org/ontology/starring> <http://dbpedia.org/resource/John_Turturo>. <http://dbpedia.org/resource/John_Turturo> text:\"role\" text:\"New York City playwright\".}"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Barton_Fink"
              }
            } ] }
        }
      ]
    },
    {
      "id": "50",
      "answertype": "resource",
      "aggregation": "false",
      "onlydbo": "true",
      "hybrid": "true",
      "question": [
        {
          "language": "en",
          "string": "Which of the volcanoes that erupted in 1550 was named after an explorer?"
        }
      ],
      "query": {
        "pseudo": "SELECT DISTINCT ?uri WHERE { ?uri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http:/dbpedia.org/ontology/Volcano> . ?uri <http:/dbpedia.org/ontology/eruptionYear> ?y . ?uri text:\"named after\" text:\"explorer\" . FILTER (year(?y) = 1550)  }"
      },
      "answers": [
        {
          "head": {
            "vars": [
              "uri"
            ]
          },
          "results": { "bindings": [
            {
              "uri": {
                "type": "uri",
                "value": "http://dbpedia.org/resource/Krasheninnikov_(volcano)"
              }
            } ] }
        }
      ]
    }
  ]
}
