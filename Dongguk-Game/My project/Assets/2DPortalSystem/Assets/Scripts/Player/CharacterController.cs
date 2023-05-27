using System;
using UnityEngine;

public class CharacterController : MonoBehaviour
{
    // Move player in 2D space
    public float maxSpeed = 3.4f;
    public float jumpHeight = 6.5f;
    public float gravityScale = 1.5f;

    [HideInInspector]public float multySpeed = 0f;

    float moveDirection = 0;
    bool isGrounded = false;
    Rigidbody2D r2d;
    Collider2D mainCollider;

    private InputSystem Inputs;

    private void Awake()
    {
        Inputs = FindObjectOfType<InputSystem>();
    }

    // Use this for initialization
    void Start()
    {
        r2d = GetComponent<Rigidbody2D>();
        mainCollider = GetComponent<Collider2D>();
        r2d.freezeRotation = true;
        r2d.collisionDetectionMode = CollisionDetectionMode2D.Continuous;
        r2d.gravityScale = gravityScale;
    }

    // Update is called once per frame
    void Update()
    {
        if (multySpeed > 1)
            multySpeed -= Time.deltaTime * Math.Abs(r2d.velocity.x+maxSpeed);
        if (multySpeed < -1)
            multySpeed += Time.deltaTime * Math.Abs(r2d.velocity.x-maxSpeed);
        if (multySpeed < 1 && multySpeed > -1)
            multySpeed = 0;

        moveDirection = Inputs.direction;

        // Jumping
        if (Inputs.isJump > 0 && isGrounded)
        {
            r2d.velocity = new Vector2(r2d.velocity.x, jumpHeight);
            isGrounded = false;
        }

        //maxSpeed
        if(r2d.velocity.magnitude >= jumpHeight+10f)
        {
            if(r2d.velocity.y<0)
                r2d.velocity = new Vector2(0, r2d.velocity.y + 0.5f);
            else
                r2d.velocity = new Vector2(0, r2d.velocity.y - 0.5f);

        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        isGrounded = true;
    }

    void FixedUpdate()
    {
        Bounds colliderBounds = mainCollider.bounds;
        Vector3 groundCheckPos = colliderBounds.min + new Vector3(colliderBounds.size.x * 0.5f, 0.1f, 0);

        // Apply movement velocity
        r2d.velocity = new Vector2((moveDirection) * maxSpeed + multySpeed, r2d.velocity.y);

        // Simple debug
        Debug.DrawLine(groundCheckPos, groundCheckPos - new Vector3(0, 0.3f, 0), isGrounded ? Color.green : Color.red);
    }
}
