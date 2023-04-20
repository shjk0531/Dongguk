using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Move : MonoBehaviour
{
    private Rigidbody2D rb;
    private float moveSpeed, dirx;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        moveSpeed = 3f;
    }

    // Update is called once per frame
    void Update()
    {
        dirx = Input.GetAxisRaw("Horizontal") * moveSpeed;
    }

    private void FixedUpdate()
    {
        rb.velocity = new Vector2 (dirx, 0f);
    }
}
