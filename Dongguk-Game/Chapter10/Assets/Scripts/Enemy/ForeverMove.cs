using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SocialPlatforms;

public class ForeverMove : MonoBehaviour
{
    public float speed = 1f;

    Rigidbody2D r2d;

    private void Start()
    {
        r2d = GetComponent<Rigidbody2D>();
        r2d.gravityScale = 0;
        r2d.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    private void FixedUpdate()
    {
        r2d.velocity = new Vector2(0, -speed);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.GetComponent<DestroyObject>())
        {
            Destroy(this.gameObject);
        }
    }
}
