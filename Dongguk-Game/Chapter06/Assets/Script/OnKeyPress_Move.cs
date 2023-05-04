using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnKeyPress_Move : MonoBehaviour
{
    public float speed = 2;

    float vx = 0;
    float vy = 0;
    Rigidbody2D rbody;

    // Start is called before the first frame update
    void Start()
    {
        rbody = GetComponent<Rigidbody2D>();
        rbody.gravityScale = 0;
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    // Update is called once per frame
    void Update()
    {
        vx = 0;
        vy = 0;
        if (Input.GetKey("right"))
        {
            vx = speed;
        }
        if (Input.GetKey("left"))
        {
           vx = -speed;
        }
        if (Input.GetKey("up"))
        {
            vy = speed;
        }
        if (Input.GetKey("down"))
        {
            vy = -speed;
        }
    }

    private void FixedUpdate()
    {
        rbody.velocity = new Vector2 (vx, vy);
    }
}
