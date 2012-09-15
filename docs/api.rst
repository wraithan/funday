API
===

This is a `Tastypie <http://tastypieapi.org/>`_ based API, as such in
interacting with it you can use their documentation for that: `Interacting with
Tastypie
<http://django-tastypie.readthedocs.org/en/latest/interacting.html>`_. Below are
the current points in the API.

.. http:get:: /api/v1/funday/

   List of all Funday objects.

   **Example Request**

   .. sourcecode:: http

      GET /api/v1/funday/ HTTP/1.1
      Host: fundayroulette.com
      Accept: application/json

   **Example Response**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json; charset=utf-8
      Vary: Accept
      
      {
        "meta": {
          "limit": 20,
          "next": "/api/v1/funday/?offset=20&limit=20&format=json",
          "offset": 0,
          "previous": null,
          "total_count": 1
        },
        "objects": [
          {
            "created": "2012-09-13T06:08:54.151000",
            "description": "The constraint is that the Zerg player is forbidden to make any Queens.",
            "game_type": "individual",
            "id": 1,
            "modified": "2012-09-14T10:02:42.453000",
            "name": "No Queens!",
            "protoss": false,
            "resource_uri": "/api/v1/funday/1/",
            "terran": false,
            "video": "http://day9.tv/d/Day9/day9-daily-183-funday-monday-no-queens/",
            "zerg": true
          },
        ]
      }

.. http:get:: /api/v1/funday/<id>/

   Details for an individual Funday object.

   **Example Request**

   .. sourcecode:: http

      GET /api/v1/funday/1/ HTTP/1.1
      Host: fundayroulette.com
      Accept: application/json

   **Example Response**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json; charset=utf-8
      Vary: Accept

      {
        "created": "2012-09-13T06:08:54.151000",
        "description": "The constraint is that the Zerg player is forbidden to make any Queens.",
        "game_type": "individual",
        "id": 1,
        "modified": "2012-09-14T10:02:42.453000",
        "name": "No Queens!",
        "protoss": false,
        "resource_uri": "/api/v1/funday/1/",
        "terran": false,
        "video": "http://day9.tv/d/Day9/day9-daily-183-funday-monday-no-queens/",
        "zerg": true
      }

.. http:get:: /api/v1/funday/random/

   Details for a random Funday object.

   **Example Request**

   .. sourcecode:: http

      GET /api/v1/funday/random/ HTTP/1.1
      Host: fundayroulette.com
      Accept: application/json

   **Example Response**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json; charset=utf-8
      Vary: Accept

      {
        "created": "2012-09-13T07:29:45.214000",
        "description": "At the beginning of your game, you must name three Units. For the rest of the game, you may only make those three Units (and workers/buildings, of course).",
        "game_type": "individual",
        "id": 16,
        "modified": "2012-09-13T07:29:45.215000",
        "name": "Count to Three",
        "protoss": true,
        "resource_uri": "/api/v1/funday/16/",
        "terran": true,
        "video":
        "http://day9.tv/d/Day9/day9-daily-284-funday-monday-count-to-three-encore/",
        "zerg": true
      }

