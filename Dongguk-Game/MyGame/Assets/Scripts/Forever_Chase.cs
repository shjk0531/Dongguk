using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Forever_Chase : MonoBehaviour
{

    public string targetObjectName;
    public float speed = 0;
    public float moveSpeed = 1;

    GameObject targetObject;
    Rigidbody2D rbody;


    // Start is called before the first frame update
    void Start()
    {
        targetObject = GameObject.Find(targetObjectName);
        rbody = GetComponent<Rigidbody2D>();
        rbody.gravityScale = 0;
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    // Update is called once per frame
    private void FixedUpdate()
    {
        Vector3 targetPosition = targetObject.transform.position;
        Vector3 thisPosition = this.transform.position;
        if (targetPosition.y <= thisPosition.y)
        {
            speed = moveSpeed;
        }

        Vector3 dir = (targetObject.transform.position - this.transform.position).normalized;

        float vx = dir.x * speed*2;
        float vy = dir.y * speed;
        rbody.velocity = new Vector2 (vx, vy);

        this.GetComponent<SpriteRenderer>().flipX = (vx < 0);
    }
}
